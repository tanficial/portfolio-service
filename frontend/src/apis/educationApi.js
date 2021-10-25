import axios from "axios";

const apiPath = process.env.REACT_APP_BACKEND_URL + "/education";

export const getEducationsRequest = async (userId) => {
    const response = await axios.get(`${apiPath}/user/${userId}`);
    return response.data.educations;
}

export const addEducationRequest = async (userId, school, major, degree) => {
    const response = await axios.post(`${apiPath}/user/${userId}`, { school, major, degree });
    return response.data.itemId;
};

export const updateEducationRequest = async (educationId, school, major, degree) => {
    await axios.patch(`${apiPath}/${educationId}`, { school, major, degree });
};

export const deleteEducationRequest = async (educationId) => {
    await axios.delete(`${apiPath}/${educationId}`);
};