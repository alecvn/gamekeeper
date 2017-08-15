import {
    FETCH_EVENTS_REQUEST,
    FETCH_EVENTS_SUCCESS,
    FETCH_EVENTS_FAILURE
} from '../actions'

function events(
    state = {
	isFetching: false,
	events: []
    },
    action) {
    switch (action.type) {
	case FETCH_EVENTS_REQUEST:
	    return Object.assign({}, state, {
		isFetching: true
	    })
	case FETCH_EVENTS_SUCCESS:
	    return Object.assign({}, state, {
		isFetching: false,
		events: action.events
	    })
	case FETCH_EVENTS_FAILURE:
	    return Object.assign({}, state, {
		isFetching: false
	    })
	default:
	    return state
    }
}

export default events
