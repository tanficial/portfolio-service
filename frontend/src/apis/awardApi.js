import axios from "axios";
const apiPath = process.env.REACT_APP_BACKEND_URL + "/award";

export const getAwardsRequest = async (userId) => {
    const response = await axios.get(`${apiPath}/user/${userId}`);
    return response.data.awards;
}

export const addAwardRequest = async (userId, title, detail) => {
    const response = await axios.post(`${apiPath}/user/${userId}`, { title, detail });
    return response.data.itemId;
}

export const updateAwardRequest = async (awardId, title, detail) => {
    await axios.patch(`${apiPath}/${awardId}`, { title, detail });
}

export const deleteAwardRequest = async (awardId) => {
    await axios.delete(`${apiPath}/${awardId}`);
}