const Hapi = require("@hapi/hapi");
const routes = require("./routes");
require("dotenv").config();

const init = async () => {
  const server = Hapi.server({
    port: process.env.PORT || 9000,
    host: "0.0.0.0", // Ubah dari localhost ke 0.0.0.0 agar bisa diakses dari luar
    routes: { cors: { origin: ["*"] } },
  });

  server.route(routes);

  await server.start();
  console.log(`Server berjalan di ${server.info.uri}`);
};

process.on('unhandledRejection', (err) => {
  console.log(err);
  process.exit(1);
});

init();