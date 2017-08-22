import 'babel-polyfill'

import React from 'react'
import { render } from 'react-dom'
import { createStore, applyMiddleware } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension';
import { Provider } from 'react-redux'
import thunk from 'redux-thunk';
// import { createLogger } from 'redux-logger'
import reducer from './reducers'
import App from './containers/App'

// const middleware = [ thunk ];
console.log(process.env.NODE_ENV);
//if (process.env.NODE_ENV !== 'production') {
//    console.log(process.env);
    //    middleware.push(createLogger());
//}


const store = createStore(
    reducer,
    composeWithDevTools(
	applyMiddleware(
	    thunk
	)
    )
);

render(
    <Provider store={store}>
	<App />
    </Provider>,
    document.getElementById('container')
)

