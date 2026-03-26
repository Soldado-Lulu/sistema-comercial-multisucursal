import TopBar from "@/components/layout/TopBar";
import Footer from "@/components/layout/Footer";
import MenuButton from "@/components/ui/MenuButton";

const menuOptions = [
  { title: "Vender", href: "/ventas",icon: "/icons/venta.png" },
  { title: "Almacenes", href: "/almacenes", icon: "/icons/almacen.png" },
  { title: "Reportes", href: "/reportes", icon: "/icons/reporte.png" },
  { title: "Agregar Productos", href: "/productos/nuevo", icon: "/icons/producto.png" },
];

export default function HomePage() {
  return (
    <main className="home">
      <div className="home__container">
        <TopBar
          branchName="Nombre de la sucursal"
          userName="Nombre de la persona registrada"
        />

        <section className="menu-grid">
          {menuOptions.map((item) => (
            <MenuButton
              key={item.href}
              title={item.title}
              href={item.href}
              icon={item.icon}
            />
          ))}
        </section>

        <Footer />
      </div>
    </main>
  );
}