import React from 'react';
import SymptomsList from "./symptoms-list";


class SymptomsSearch extends React.Component {
    constructor(props) {
        super(props);
        this.state = {selectedPositives: [], selectedNegatives: [], filter: ""}
    };

    changeHandler(sym, val) {
        let selectedPos = this.state.selectedPositives;
        let selectedNeg = this.state.selectedNegatives;


        if (selectedPos.includes(sym)) {
            if (val !== 'true') { // for false and null, remove
                selectedPos = selectedPos.filter(e => e !== sym);
            }
        } else if (val === 'true') {
            selectedPos.push(sym);
        }

        if (selectedNeg.includes(sym)) {
            if (val !== 'false') { // for true and null, remove
                selectedNeg = selectedNeg.filter(e => e !== sym);
            }
        } else if (val === 'false') {
            selectedNeg.push(sym);
        }

        this.setState({selectedPositives: selectedPos, selectedNegatives: selectedNeg});
    };

    onConfirm = () => {
        let pos = this.state.selectedPositives;
        let neg = this.state.selectedNegatives;
        this.setState({selectedPositives: [], selectedNegatives: [], filter: ""})
        this.props.submitFilters(pos, neg);
    };

    render() {
        return (
            <div className="middle-area">
                <div className="overflow-hidden">
                    <div className="header"> Possible symptoms</div>
                    <div className='confirm-botton' onClick={this.onConfirm}>Confirm</div>
                    <input
                        placeholder={"Search symptoms"}
                        style={{
                            padding: '5px',
                            marginLeft: '50px',
                            width: '370px',
                            marginTop: '20px',
                            fontSize: '14px'
                        }}
                        type="text"
                        value={this.state.filter}
                        onChange={(evt) => {
                            this.setState({filter: evt.target.value})
                        }}
                    />
                </div>
                <SymptomsList symptoms={this.props.symptoms.filter(symptom => {
                    return symptom.indexOf(this.state.filter) > -1
                })} changeHandler={this.changeHandler.bind(this)}/>
            </div>)
    }
}

export default SymptomsSearch;
