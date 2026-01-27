const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// GET API
app.get("/api/message", (req, res) => {
  res.json({ message: "Hello from Backend 👋" });
});

// POST API
app.post("/api/name", (req, res) => {
  const name = req.body.name;
  res.json({ reply: `Hello ${name} 👋 from Backend` });
});

// Server start
app.listen(5000, () => {
  console.log("Backend running at http://localhost:5000");
});
