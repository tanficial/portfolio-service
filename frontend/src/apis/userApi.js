import axios from "axios";

const apiPath = process.env.REACT_APP_BACKEND_URL + "/user";

export const getUserRequest = async (userId) => {
    const response = await axios.get(`${apiPath}/${userId}`);
    return response.data.user
}

export const updateUserRequest = async (userId, name, description) => {
    await axios.patch(`${apiPath}/${userId}`, { name, description });
}

export const updateProfileImage = async (userId, image) => {
    await axios.patch(`${apiPath}/${userId}/image`, { image });
}