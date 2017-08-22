import React from 'react'
import { connect } from 'react-redux'
import { Nav, Navbar, NavDropdown, NavItem, MenuItem, Breadcrumb } from 'react-bootstrap'
import { loadPlayers, fetchEvents } from '../actions'

class Events extends React.Component {
    constructor(props) {
	super(props);
	this.handleSelect = this.handleSelect.bind(this);
    }

    componentDidMount() {
	const { dispatch } = this.props;
	dispatch(fetchEvents());

    }

    handleSelect(selectedKey) {
	const { dispatch } = this.props;
	//console.log(this.props.events.events[selectedKey]);
	dispatch(loadPlayers(this.props.events.events[selectedKey]['players_points']));
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
		<Breadcrumb>
		    <Breadcrumb.Item active>
			League
		    </Breadcrumb.Item>
		    <Breadcrumb.Item>
			Matches
		    </Breadcrumb.Item>
		    <Breadcrumb.Item>
			Games
		    </Breadcrumb.Item>
		    <Breadcrumb.Item>
			All
		    </Breadcrumb.Item>
		</Breadcrumb>
		<Nav bsStyle="pills" stacked activeKey={0} onSelect={this.handleSelect}>
		    {this.props.events.events.map((event, i) =>
			<NavItem eventKey={i} key={i} >{event.name}</NavItem> // className={(i == 0) ? "active" : ""}
		    )}
		</Nav>
	    </div>
	)
    }
}

function mapStateToProps(state, ownProps) {
    const {
	isFetching,
	events: events,
	selected_events: selected_events
    } = state || {
	isFetching: true,
	events: [],
	selected_events: []
    }

    return {
	events,
	isFetching
    }
}

export default connect(mapStateToProps)(Events)
