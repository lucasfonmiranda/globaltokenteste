import React from 'react';
import AppBar from 'material-ui/AppBar';
import FlatButton from 'material-ui/FlatButton';
// import VideoPlayer from '../components/VideoPlayer';

class VideoContainer extends React.Component{
	render(){
		return (<div>
			<AppBar
	          title={
	              <img src="http://www.solidareasy.com/wp-content/uploads/2017/08/SEO-google-1.png"/>
	            }
	          showMenuIconButton
	          className="app-bar"/>
	          <div>
	          <h3>TESTE </h3>
	          </div>

			</div>
			);
	}
} 
export default VideoContainer;