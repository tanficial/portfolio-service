import axios from "axios";

const apiPath = process.env.REACT_APP_BACKEND_URL + "/license";

export const getLicensesRequest = async (userId) => {
    const response = await axios.get(`${apiPath}/user/${userId}`);
    return response.data.licenses;
}

export const addLicenseRequest = async (userId, title, organization, acquisition) => {
    const response = await axios.post(`${apiPath}/user/${userId}`, { title, organization, acquisition });
    return response.data.itemId;
}

export const updateLicenseRequest = async (licenseId, title, organization, acquisition) => {
    await axios.patch(`${apiPath}/${licenseId}`, { title, organization, acquisition });
}

export const deleteLicenseRequest = async (licenseId) => {
    await axios.delete(`${apiPath}/${licenseId}`);
}
