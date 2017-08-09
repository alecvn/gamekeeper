import React from 'react'
import { connect } from 'react-redux'
import { Col } from 'react-bootstrap'

import Events from '../containers/Events'
import CurrentEvent from '../containers/CurrentEvent'
import Players from '../containers/Players'
import styles from '../../css/main.css'


let Body = ({ dispatch }) => {
    let input

    return (
	<div className={styles.bg}>
	    <Col md={3}>
		<Events />
	    </Col>
	    <Col md={6}>
		<CurrentEvent />
	    </Col>
	    <Col md={3}>
		<Players />
	    </Col>
	</div>
    )
}
Body = connect()(Body)

export default Body
