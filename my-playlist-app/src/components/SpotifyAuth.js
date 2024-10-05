import axios from 'axios';

const client_id = 'd22946da551c4fdd96f4d4785cb941d8'; // Replace with your Client ID
const client_secret = '6ec7b1bc22ec4ac3bedb9af89c09c3f8'; // Replace with your Client Secret

export const getAccessToken = async () => {
  const response = await axios.post('https://accounts.spotify.com/api/token', 'grant_type=client_credentials', {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': 'Basic ' + btoa(client_id + ':' + client_secret),
    },
  });

  return response.data.access_token;
};
