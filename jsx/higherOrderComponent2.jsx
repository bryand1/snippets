var config = require('path/to/configuration');

var enhanceComponent = (Component) =>
  class Enhance extends React.Component {
    render() {
      return (
        <Component
          {...this.props}
          title={ config.appTitle }
        />
      )
    }
  };

var OriginalTitle = ({ title }) => <h1>{ title }</h1>
var EnhancedTitle = enhanceComponent(OriginalTitle);
