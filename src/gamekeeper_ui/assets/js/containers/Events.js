import React from 'react'
import { connect } from 'react-redux'
import { Nav, Navbar, NavDropdown, NavItem, MenuItem, Breadcrumb, Tabs, Tab } from 'react-bootstrap'
import { loadPlayers, fetchEvents, fetchPlayers, loadEvents } from '../actions'

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
	}
    }

    handleHistory(key) {
	const { dispatch } = this.props
	console.log(key)
    }

    render() {
	let top_event_name = "None"
	let top_event = this.props.events.events[0]
	if (top_event !== undefined) {
	    top_event_name = top_event.name
	}

	return (
	    <div>
		<Navbar>
		    <Navbar.Header>
			<Navbar.Brand>
			    Events
			</Navbar.Brand>
		    </Navbar.Header>
		</Navbar>
		<Tabs activeKey={0} onSelect={this.handleHistory} id="controlled-tab-example">
		    {this.props.events.focussed_events.map((event, i) =>
			<Tab key={i} eventKey={i} title={event.parent}>League</Tab>
		    )}
		</Tabs>
		<Nav bsStyle="pills" stacked activeKey={0} onSelect={this.handleSelect}>
		    {this.props.events.focussed_events.map((event, i) =>
			<NavItem eventKey={i} key={i} >{event.name}</NavItem> // className={(i == 0) ? "active" : ""}
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
	focussed_events: focussed_events
    } = state || {
	isFetching: true,
	events: [],
	focussed_events: []
    }

    return {
	isFetching,
	events,
	focussed_events
    }
}

export default connect(mapStateToProps)(Events)
