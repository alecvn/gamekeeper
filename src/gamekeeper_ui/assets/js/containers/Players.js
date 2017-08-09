import React from 'react'
import { connect } from 'react-redux'
import { Nav, Navbar, NavDropdown, NavItem, MenuItem, Table } from 'react-bootstrap'

let Players = ({ dispatch }) => {
    let input

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
			<MenuItem eventKey={3.1}>Keith</MenuItem>
			<MenuItem eventKey={3.2}>Alec</MenuItem>
			<MenuItem eventKey={3.3}>Andrew</MenuItem>
			<MenuItem eventKey={3.4}>Tshepo</MenuItem>
		    </NavDropdown>
		</Nav>
	    </Navbar>
	    <Table striped bordered condensed hover>
		<thead>
		    <tr>
			<th>#</th>
			<th>First Name</th>
			<th>Last Name</th>
			<th>Username</th>
		    </tr>
		</thead>
		<tbody>
		    <tr>
			<td>1</td>
			<td>Mark</td>
			<td>Otto</td>
			<td>@mdo</td>
		    </tr>
		    <tr>
			<td>2</td>
			<td>Jacob</td>
			<td>Thornton</td>
			<td>@fat</td>
		    </tr>
		    <tr>
			<td>3</td>
			<td colSpan="2">Larry the Bird</td>
			<td>@twitter</td>
		    </tr>
		</tbody>
	    </Table>
	</div>
    )
}
Players = connect()(Players)

export default Players

