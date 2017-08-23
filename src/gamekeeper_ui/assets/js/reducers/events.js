import {
    FETCH_EVENTS_REQUEST,
    FETCH_EVENTS_SUCCESS,
    FETCH_EVENTS_FAILURE,
    LOAD_EVENTS
} from '../actions'

function events(
    state = {
	isFetching: false,
	events: [],
	focussed_events: []
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
		events: action.events,
		focussed_events: [action.events[0]],
	    })
	case LOAD_EVENTS:
	    return Object.assign({}, state, {
		focussed_events: state.events.filter(function(event) {return action.events.includes(event.id)}),
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
