import axios from "axios";

const BASE_URL = process.env.REACT_APP_API_URL

export const sendMsgToChatbot = async(msg) => {
  try{
    console.log(`juso : ${BASE_URL}/api/chat`);
    const response = await axios.post(
      `${BASE_URL}/api/chat`,
      {message: msg},
      {headers: {"Content-Type": "application/json"}}
    );
    return response.data
  }catch(error){
    console.error(`🥺 요청 실패 : ${error}`);
    throw error;
  }
};