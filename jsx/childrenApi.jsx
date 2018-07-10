export default function App() {
  return (
    <Header>
      <Navigation />
    </Header>
  );
}

export default function Header({ children }) {
  return <header>{ children }</header>;
}
