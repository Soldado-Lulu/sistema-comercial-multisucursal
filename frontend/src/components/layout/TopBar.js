const TopBar = ({ branchName, userName }) => {
  return (
    <div className="topbar">
      <h1 className="topbar__branch">{branchName}</h1>
      <p className="topbar__user">{userName}</p>
    </div>
  );
};

export default TopBar;