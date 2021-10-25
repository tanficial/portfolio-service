import axios from "axios";

const apiPath = process.env.REACT_APP_BACKEND_URL + "/project";

export const getProjectsRequest = async (userId) => {
    const response = await axios.get(`${apiPath}/user/${userId}`);
    return response.data.projects;
}

export const addProjectRequest = async (userId, title, detail, startDate, endDate) => {
    const response = await axios.post(`${apiPath}/user/${userId}`, { title, detail, start_date: startDate, end_date: endDate });
    return response.data.itemId;
};

export const updateProjectRequest = async (projectId, title, detail, startDate, endDate) => {
    await axios.patch(`${apiPath}/${projectId}`, { title, detail, start_date: startDate, end_date: endDate });
};

export const deleteProjectRequest = async (projectId) => {
    await axios.delete(`${apiPath}/${projectId}`);
};

