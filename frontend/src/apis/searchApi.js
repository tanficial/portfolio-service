import axios from "axios";

const apiPath = process.env.REACT_APP_BACKEND_URL + "/user";

export const searchUsers = async (query) => {
    const response = await axios.get(`${apiPath}?query=${query}`);
    return response.data.users;
};