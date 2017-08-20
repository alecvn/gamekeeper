import fetch from 'isomorphic-fetch'

export const FETCH_PLAYERS_REQUEST = 'FETCH_PLAYERS_REQUEST'
export const FETCH_PLAYERS_SUCCESS = 'FETCH_PLAYERS_SUCCESS'
export const FETCH_PLAYERS_FAILURE = 'FETCH_PLAYERS_FAILURE'

export const FETCH_EVENTS_REQUEST = 'FETCH_EVENTS_REQUEST'
export const FETCH_EVENTS_SUCCESS = 'FETCH_EVENTS_SUCCESS'
export const FETCH_EVENTS_FAILURE = 'FETCH_EVENTS_FAILURE'


function requestPlayers() {
    return {
	type: 'FETCH_PLAYERS_REQUEST'
    }
}

function fetchPlayersFailed() {
    return {
	type: 'FETCH_PLAYERS_FAILURE', error: 'GET Players failed'
    }
}

function fetchPlayersSucceeded(json) {
    return {
	type: 'FETCH_PLAYERS_SUCCESS',
	players: json //.children.map(child => child.data)
    }
}

export function loadPlayers(json) {
    return {
	type: 'FETCH_PLAYERS_SUCCESS',
	players: json //.children.map(child => child.data)
    }
}

export function fetchPlayers() {
    // Thunk middleware knows how to handle functions.
    // It passes the dispatch method as an argument to the function,
    // thus making it able to dispatch actions itself.

    return function (dispatch) {
	// First dispatch: the app state is updated to inform
	// that the API call is starting.

	dispatch(requestPlayers())

	// The function called by the thunk middleware can return a value,
	// that is passed on as the return value of the dispatch method.

	// In this case, we return a promise to wait for.
	// This is not required by thunk middleware, but it is convenient for us.

	return fetch("http://gamekeeper.impd.co.za/players/?format=json")
	    .then(
		response => response.json(),
		// Do not use catch, because that will also catch
		// any errors in the dispatch and resulting render,
		// causing an loop of 'Unexpected batch number' errors.
		    // https://github.com/facebook/react/issues/6895
		error => console.log('An error occured.', error)
	    )
	    .then(json =>
		// We can dispatch many times!
		// Here, we update the app state with the results of the API call.

		    dispatch(fetchPlayersSucceeded(json))
	    )
    }
}

function requestEvents() {
    return {
	type: 'FETCH_EVENTS_REQUEST'
    }
}

function fetchEventsFailed() {
    return {
	type: 'FETCH_EVENTS_FAILURE', error: 'GET Events failed'
    }
}

function fetchEventsSucceeded(json) {
    return {
	type: 'FETCH_EVENTS_SUCCESS',
	events: json //.children.map(child => child.data)
    }
}

export function fetchEvents() {
    // Thunk middleware knows how to handle functions.
    // It passes the dispatch method as an argument to the function,
    // thus making it able to dispatch actions itself.

    return function (dispatch) {
	// First dispatch: the app state is updated to inform
	// that the API call is starting.

	dispatch(requestEvents())

	// The function called by the thunk middleware can return a value,
	// that is passed on as the return value of the dispatch method.

	// In this case, we return a promise to wait for.
	// This is not required by thunk middleware, but it is convenient for us.

	return fetch("http://gamekeeper.impd.co.za/events/?format=json")
	    .then(
		response => response.json(),
		// Do not use catch, because that will also catch
		// any errors in the dispatch and resulting render,
		// causing an loop of 'Unexpected batch number' errors.
		    // https://github.com/facebook/react/issues/6895
		error => console.log('An error occured.', error)
	    )
	    .then(json =>
		// We can dispatch many times!
		// Here, we update the app state with the results of the API call.

		    dispatch(fetchEventsSucceeded(json))
	    )
    }
}
