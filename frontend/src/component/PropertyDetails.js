import React, { Component } from 'react'

export default class PropertyDetails extends Component {
    render() {
        // If property Details exist, Display below
        return (
            <div className={"col"}>
                {this.props.title}
                <div className={'content'}>
                    {Object.keys(this.props.text).length > 0 ? (
                        <pre>
                            {JSON.stringify(this.props.text, null, 2)}
                        </pre>

                    ) : null}
                </div>
                {Object.keys(this.props.text).length > 0 ? (
                    <div className={'Clear'} onClick={this.props.clear}>Clear</div>
                ) : null}
            </div>
        )
    }
}
