import React from 'react'
import { connect } from 'react-redux'
import { Nav, Navbar, NavDropdown, NavItem, MenuItem, Table } from 'react-bootstrap'
import { fetchPlayers } from '../actions'


class Players extends React.Component {
    constructor(props) {
	super(props);
    }

    componentDidMount() {
	const { dispatch } = this.props;
	// dispatch(fetchPlayers());
    }

    render() {
	return (
	    <div>
		<Navbar>
		    <Navbar.Header>
			<Navbar.Brand>
			    Players
			</Navbar.Brand>
		    </Navbar.Header>
		    <Nav>
			<NavDropdown eventKey={3} title="Add to event" id="basic-nav-dropdown">
	    {this.props.players.players.map((player, i) =>
		<MenuItem key={i}
			  eventKey={3.1}>
		    {player.full_name}
		</MenuItem>)}
			</NavDropdown>
		</Nav>
		</Navbar>
		<Table striped bordered condensed hover>
		    <thead>
			<tr>
			    <th>#</th>
			    <th>Name</th>
			    <th>Points</th>
			</tr>
		    </thead>
		    <tbody>
			{this.props.players.players.map((player, i) =>
			    <tr key={i}>
				<td>{i+1}</td>
				<td>{player.full_name}</td>
				<td>{player.points}</td>
			    </tr>
			)}
		    </tbody>
		</Table>
	    </div>
	)
    }
    /* render() {
       const persons = this.state.person.map((item, i) => {
       return <div>
       <h1>{item.name.first}</h1>
       <span>{item.cell}, {item.email}</span>
       </div>
       });

       return <div id="layout-content" className="layout-content-wrapper">
       <div className="panel-list">{ persons }</div>
       </div>
     * }*/
    
}

/* Players = connect()(Players)
 * 
 * export default Players
 * */
function mapStateToProps(state, ownProps) {
    // http://127.0.0.1:8000/events/7/players/3/details/
    const {
	isFetching,
	players: players
    } = state || {
	isFetching: true,
	players: []
    }

    return {
	players,
	isFetching
    }
}

export default connect(mapStateToProps)(Players)

