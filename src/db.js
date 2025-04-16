const mysql = require("mysql2/promise");

const pool = mysql.createPool({
  host: 'sql12.freesqldatabase.com',   // ganti dengan host kamu
  user: 'sql1234567',                  // username dari dashboard
  password: 'sYp4KnVdAq',            // password kamu
  database: 'sql1234567',              // database name kamu
  port: 3306,                           // default port
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

pool
  .getConnection()
  .then((conn) => {
    console.log("Database connected!");
    conn.release();
  })
  .catch((err) => {
    console.error("Database connection failed: ", err.message);
  });

module.exports = pool;
