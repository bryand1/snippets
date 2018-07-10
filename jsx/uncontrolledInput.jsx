// Uncontrolled inputs are an anti-pattern and should be avoided

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
        defaultValue={ this.state.value } 
        onChange={ this._change }
        ref={ input => this.input = input }
      />
    )
  }
  _handleInputChange() {
    this.setState({ value: this.input.value });
  }
};