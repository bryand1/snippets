function UserName({ children }) {
  return (
    <div>
      <b>{ children.lastName }</b>,
      { children.firstName }
    </div>
  );
}

function App() {
  const user = {
    firstName: 'Krasimir',
    lastName: 'Tsonev'
  };
  return (
    <UserName>{ user }</UserName>
  );
}
