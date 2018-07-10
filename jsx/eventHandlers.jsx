class Form extends React.component {
  constructor(props) {
    super(props);
    this._onNameChange = this._onFieldChange.bind(this, 'name');
    this._onPasswordChange = this._onFieldChange.bind(this, 'password');
  }
  render() {
    return (
      <form>
        <input onChange={ this._onNameChange } />
        <input onChange={ this._onPasswordChange } />
      </form>
    );
  }
  _onFieldChange(field, event) {
    console.log(`${ field } changed to ${ event.target.value }`);
  }
};
