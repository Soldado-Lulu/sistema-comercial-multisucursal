import "./glogals.css";

export const metadata = {
  title: "Sistema Comercial Multisucursal",
  description: "Sistema web de inventario y ventas",
};

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}