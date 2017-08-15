import React from 'react'
import { connect } from 'react-redux'
import { Nav, Navbar, NavDropdown, NavItem, MenuItem, Breadcrumb } from 'react-bootstrap'

let Events = ({ dispatch }) => {
    let input


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
		<Breadcrumb.Item href="#">
		    Home
		</Breadcrumb.Item>
		<Breadcrumb.Item href="http://getbootstrap.com/components/#breadcrumbs">
		    Library
		</Breadcrumb.Item>
		<Breadcrumb.Item active>
		    Data
		</Breadcrumb.Item>
	    </Breadcrumb>
	    <Nav bsStyle="pills" stacked activeKey={1}>
		<NavItem eventKey={1} href="/home">NavItem 1 content</NavItem>
		<NavItem eventKey={2} title="Item">NavItem 2 content</NavItem>
		<NavItem eventKey={3} disabled>NavItem 3 content</NavItem>
	    </Nav>
	</div>

    )
}
Events = connect()(Events)

export default Events

