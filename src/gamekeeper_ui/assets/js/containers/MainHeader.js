import React from 'react'
import { connect } from 'react-redux'
import { PageHeader, Nav, Navbar, NavDropdown, NavItem, MenuItem } from 'react-bootstrap'

let MainHeader = ({ dispatch }) => {
    let input

    return (
	<div>
	    <PageHeader>
		Gamekeeper
	    </PageHeader>
	    <Navbar>
		<Navbar.Header>
		    <Navbar.Brand>
			Games
		    </Navbar.Brand>
		</Navbar.Header>
		<Nav>
		    <NavItem eventKey={1} href="#">Darts</NavItem>
		    <NavItem eventKey={2} href="#">Magic</NavItem>
		</Nav>
	    </Navbar>
	</div>
    )
}
MainHeader = connect()(MainHeader)

export default MainHeader
