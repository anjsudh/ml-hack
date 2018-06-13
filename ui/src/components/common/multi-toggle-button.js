import React from "react";
import {isEqual} from "lodash";

class MultiToggle extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			options: this.props.options || [],
			selected: (this.props.selected !== undefined) ? this.props.selected : (this.props.options && this.props.options.length ? this.props.options[0].key : "")
		};
	}

	componentWillReceiveProps(nextProps) {
		if(!isEqual(nextProps, this.props)) {
			this.setState(
				{
					options: nextProps.options || [],
					selected: (this.props.selected !== undefined) ? this.props.selected : (nextProps.options && nextProps.options.length ? nextProps.options[0].key : "")
				}
			)
		}
	}

	onClick = (option) => {
		if(this.state.selected !== option.key) {
			this.setState({ selected: option.key });
			if(this.props.onChange) {
				this.props.onChange(option.key);
			}
		}
	}

	render() {
		return (
			<ul className="multi-toggle">
				{
					this.state.options.map((option, index) => {
						return (
							<li key={index} className={option.key === this.state.selected ? "toggle-li selected" : "toggle-li"} onClick={() => { this.onClick(option) }}>{option.value}</li>
						)
					})
				}
			</ul>
		);
	}
}

export default MultiToggle;