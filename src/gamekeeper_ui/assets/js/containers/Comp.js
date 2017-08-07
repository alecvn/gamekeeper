import React from 'react'
import { connect } from 'react-redux'

let Comp = ({ dispatch }) => {
    let input

    return (
	<div>
        <button type="submit">
        Add Todo
        </button>
	</div>
    )
}
Comp = connect()(Comp)

export default Comp
