import { combineReducers } from 'redux'
import players from './players'
import events from './events'

const gamekeeperApp = combineReducers({
    players,
    events
})

export default gamekeeperApp
