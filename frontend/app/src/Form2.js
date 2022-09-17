import React from "react";

export const Form2 = ({ onSubmit }) => {
  return (
    <form onSubmit={onSubmit}>
      <div className="form-group">
        <label htmlFor="name">Shop</label>
      </div>
      <div className="form-group">
        <button className="form-control btn btn-primary" type="submit">
          buy flowers
        </button>
        <button className="form-control btn btn-primary" type="submit">
          buy wat er
        </button>
        <button className="form-control btn btn-primary" type="submit">
          buy gnomes
        </button>
        <button className="form-control btn btn-primary" type="submit">
          buy background
        </button>
      </div>
    </form>
  );
};
export default Form2;
