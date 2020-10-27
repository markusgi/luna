import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from '../pages/Home';

const Routes = () => {
	return (
		<Router>
			<Switch>
				<Route exact path='/' component={Home} />
				{/* <Route exact path='/login' component={Login} /> */}
			</Switch>
		</Router>
	);
};

export default Routes;
