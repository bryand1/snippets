const Title = function () {
  return <h1>Hello there!</h1>;
}

const Header = function ({ title, children }) {
  return (
    <header>
      { title }
      { children }
    </header>
  );
}

function App() {
  return (
    <Header title={ <Title /> }>
      <Navigation />
    </Header>
  );
}
