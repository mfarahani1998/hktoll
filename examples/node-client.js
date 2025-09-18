// Minimal Node.js client calling the HTTP API
import fetch from "node-fetch";
const body = {
  coords: [[114.1582,22.2799],[114.1640,22.2801],[114.1721,22.2975]],
  vehicle: "private_car",
  when: "2025-09-17T08:30:00+08:00"
};
const res = await fetch("http://localhost:8000/v1/tolls/route", {
  method: "POST",
  headers: {"content-type":"application/json"},
  body: JSON.stringify(body)
});
console.log(await res.json());
