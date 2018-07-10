var enhanceComponent = (Component) =>
  class Enhance extends React.Component {
    constructor(props) {
      super(props);
      this.state = { remoteTitle: null };
    }
    componentDidMount() {
      fetchRemoteData('path/to/endpoint').then(data => {
        this.setState({ remoteTitle: data.title });
      });
    }
    render() {
      return (
        <Component
          {...this.props}
          title={ config.appTitle }
          remoteTitle={ this.state.remoteTitle }
        />
      )
    }
  }

var OriginalTitle = ({ title, remoteTitle }) =>
  <h1>{ title }{ remoteTitle }</h1>;
var EnhancedTitle = enhanceComponent(OriginalTitle);
