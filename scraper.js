const chromium = require('chrome-aws-lambda');
const puppeteer = require('puppeteer-core');
const AWS = require('aws-sdk');
const s3 = new AWS.S3();

async function scrapeIndeedJobs() {
    const browser = await puppeteer.launch({
        args: [...chromium.args],
        defaultViewport: chromium.defaultViewport,
        executablePath: await chromium.executablePath,
        headless: true,
    });
    const page = await browser.newPage();

    // Navigate to Indeed job search page
    await page.goto('https://www.indeed.com/jobs?q=Software+Engineer&l=United+States');

    // Wait for job listings to load
    await page.waitForSelector('.jobsearch-SerpJobCard');

    // Extract job data
    const jobs = await page.evaluate(() => {
        const jobElements = document.querySelectorAll('.jobsearch-SerpJobCard');
        return Array.from(jobElements).map(jobElement => ({
            title: jobElement.querySelector('h2.title').innerText.trim(),
            company: jobElement.querySelector('span.company').innerText.trim(),
            location: jobElement.querySelector('div.recJobLoc').dataset.rcLoc
        }));
    });

    await browser.close();

    // Save the scraped data to an S3 bucket
    const params = {
        Bucket: 'temporary_intermediary',  // S3 bucket
        Key: `scraped-jobs-${Date.now()}.json`,  // File name with timestamp
        Body: JSON.stringify(jobs),
        ContentType: 'application/json'
    };

    try {
        const data = await s3.upload(params).promise();
        console.log(`File uploaded successfully. ${data.Location}`);
    } catch (err) {
        console.error("Error uploading file: ", err);
    }

    return jobs;
}

exports.handler = async (event) => {
    const jobListings = await scrapeIndeedJobs();
    return {
        statusCode: 200,
        body: JSON.stringify(jobListings)
    };
};
