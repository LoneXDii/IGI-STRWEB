const dotenv = require('dotenv');
dotenv.config();
const { BlobServiceClient } = require('@azure/storage-blob');

const blobServiceClient = BlobServiceClient.fromConnectionString(process.env.AZURE_CONNECTION);
const containerClient = blobServiceClient.getContainerClient(process.env.AZURE_CONTAINER);

async function initializeContainer() {
    await containerClient.createIfNotExists();
    return containerClient;
}

module.exports = initializeContainer;