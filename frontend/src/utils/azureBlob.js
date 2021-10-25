import { BlobServiceClient } from "@azure/storage-blob";

const sasURL = process.env.REACT_APP_SAS_URL;
const blobServiceClient = new BlobServiceClient(sasURL);

export const uploadImage = async (userId, file) => {
    const extensionIdx = file.name.indexOf(".");
    const extension = file.name.slice(extensionIdx);

    const containerClient = blobServiceClient.getContainerClient("image");
    const blobName = `userProfileImage${userId}` + new Date().getTime() + extension;
    const blockBlobClient = containerClient.getBlockBlobClient(blobName);
    await blockBlobClient.upload(file, Buffer.byteLength(file));

    const idx = blockBlobClient.url.indexOf("?");
    return blockBlobClient.url.slice(0, idx);
}

export const deleteImage = async (blobURL) => {
    const blobIdx = blobURL.indexOf("userProfileImage");
    const blobName = blobURL.slice(blobIdx);

    const containerClient = blobServiceClient.getContainerClient("image");
    const blockBlobClient = containerClient.getBlockBlobClient(blobName);

    await blockBlobClient.deleteIfExists();
}