import React from 'react'
import { render } from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
// import { createLogger } from 'redux-logger'
import reducer from './reducers'
import App from './containers/App'

// const middleware = [ thunk ];
// if (process.env.NODE_ENV !== 'production') {
//   middleware.push(createLogger());
// }

const store = createStore(reducer)

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('container')
)

// var React = require('react')
// var ReactDOM = require('react-dom')

// var Hello = React.createClass ({
//     render: function() {
//         return (
//             <h1>
//             Hello, React!
//             </h1>
//         )
//     }
// })

// ReactDOM.render(<Hello />, document.getElementById('container'))
