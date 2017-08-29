import {
    FETCH_EVENTS_REQUEST,
    FETCH_EVENTS_SUCCESS,
    FETCH_EVENTS_FAILURE,
    LOAD_EVENTS,
    ADD_TO_EVENTS_TAB
} from '../actions'

function events(
    state = {
	isFetching: false,
	events: [],
	focussed_events: [],
	tabbed_events: [],
	active_tab_idx: 0
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
	case ADD_TO_EVENTS_TAB:
	    return Object.assign({}, state, {
		active_tab_idx: action.idx,
		tabbed_events: state.tabbed_events.concat(state.events.filter(function(event) {return action.event_id == event.id})),
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
