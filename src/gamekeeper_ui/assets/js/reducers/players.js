import {
    FETCH_PLAYERS_REQUEST,
    FETCH_PLAYERS_SUCCESS,
    FETCH_PLAYERS_FAILURE
} from '../actions'

function players(
    state = {
	isFetching: false,
	players: []
    },
    action) {
    switch (action.type) {
	case FETCH_PLAYERS_REQUEST:
	    return Object.assign({}, state, {
		isFetching: true
	    })
	case FETCH_PLAYERS_SUCCESS:
	    return Object.assign({}, state, {
		isFetching: false,
		players: action.players
	    })
	case FETCH_PLAYERS_FAILURE:
	    return Object.assign({}, state, {
		isFetching: false
	    })
	default:
	    return state
    }
}

export default players
