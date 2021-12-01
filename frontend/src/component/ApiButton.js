import React, { Component } from 'react'

export default class ApiButton extends Component {
    render() {
        return (
            <div className={'buttonContainer'} onClick={this.props.determineSewer}>
                {this.props.text}
            </div>
        )
    }
}
