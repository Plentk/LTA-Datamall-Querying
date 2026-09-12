const myHeaders = new Headers();
myHeaders.append("AccountKey", "");
myHeaders.append("accept", "application/json");

const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};

fetch("https://datamall2.mytransport.sg/ltaodataservice/BusServices?skip=500", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));