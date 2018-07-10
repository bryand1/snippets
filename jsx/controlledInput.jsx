class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: 'hello' };
    this._change = this._handleInputChange.bind(this);
  }
  render() {
    return (
      <input
        type='text'
        value={ this.state.value }
        onChange={ this._change }
      />
    );
  }
  _handleInputChange(e) {
    this.setState({ value: e.target.value });
  }
};
