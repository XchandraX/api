const mysql = require("mysql2/promise");

const pool = mysql.createPool({
  uri: 'mysql://root:OxGKiMTeskKcqphBbHxGZRLhTVYYfasH@maglev.proxy.rlwy.net:19890/railway',  // URL koneksi Railway
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

pool
  .getConnection()
  .then((conn) => {
    console.log("Database connected!");
    conn.release();  // Pastikan koneksi dilepaskan setelah digunakan
  })
  .catch((err) => {
    console.error("Database connection failed: ", err.message);
  });

module.exports = pool;
