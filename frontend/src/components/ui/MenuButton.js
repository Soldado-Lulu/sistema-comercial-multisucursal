import Link from "next/link";
import Image from "next/image";

const MenuButton = ({ title, href, icon, colorClass = "" }) => {
  return (
    <Link href={href} className={`menu-button ${colorClass}`}>
      {icon && (
        <div className="menu-button__icon">
          <Image src={icon} alt={title} width={52} height={52} />
        </div>
      )}

      <span className="menu-button__text">{title}</span>
    </Link>
  );
};

export default MenuButton;