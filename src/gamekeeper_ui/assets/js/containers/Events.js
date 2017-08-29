import React from 'react'
import { connect } from 'react-redux'
import { Nav, Navbar, NavDropdown, NavItem, MenuItem, Breadcrumb, Tabs, Tab } from 'react-bootstrap'
import { loadPlayers, fetchEvents, fetchPlayers, loadEvents, addToEventsTab, removeFromEventsTab } from '../actions'

class Events extends React.Component {
    constructor(props) {
	super(props);
	this.handleSelect = this.handleSelect.bind(this)
	this.handleHistory = this.handleHistory.bind(this)
    }

    componentDidMount() {
	const { dispatch } = this.props
	dispatch(fetchEvents())
    }

    handleSelect(selectedKey) {
	const { dispatch } = this.props
	//console.log(this.props.events.events[selectedKey])
	// dispatch(loadPlayers(this.props.events.events[selectedKey]['players_points']))
	dispatch(fetchPlayers(this.props.events.focussed_events[selectedKey].id))
	let children = this.props.events.focussed_events[selectedKey].child_events
	if (children.length > 0) {
	    dispatch(loadEvents(children))
	    dispatch(addToEventsTab(selectedKey, this.props.events.focussed_events[selectedKey].id))
	} else {
	    
	}
    }

    handleHistory(key) {
	const { dispatch } = this.props
	let children = this.props.events.tabbed_events[key].child_events
	if (children.length > 0) {
	    dispatch(loadEvents(children))
	    //dispatch(removeFromEventsTab(this.props.events.tabbed_events[key].id))
	}
    }

    render() {
	return (
	    <div>
		<Navbar>
		    <Navbar.Header>
			<Navbar.Brand>
			    Events
			</Navbar.Brand>
		    </Navbar.Header>
		</Navbar>
		<Tabs onSelect={this.handleHistory} id="blah">
		    {this.props.events.tabbed_events.map((event, i) =>
			<Tab key={i} eventKey={i} title={event.name}></Tab>
		    )}
		</Tabs>
		<Nav bsStyle="pills" stacked onSelect={this.handleSelect}>
		    {this.props.events.focussed_events.map((event, i) =>
			<NavItem eventKey={i} key={i}>{event.name}</NavItem>
		    )}
		</Nav>
	    </div>
	)
    }
}

function mapStateToProps(state, ownProps) {
    // curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:3000/api/login
    // "2012-04-23T18:25:43.511Z"
    const {
	isFetching,
	events: events,
	focussed_events: focussed_events,
	tabbed_events: tabbed_events,
	active_tab_idx
    } = state

    return {
	isFetching,
	events,
	focussed_events,
	tabbed_events,
	active_tab_idx
    }
}

export default connect(mapStateToProps)(Events)
